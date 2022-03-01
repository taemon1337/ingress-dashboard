<script>
  import { ImageUrl } from '../stores/images.js';
  import { Icon, InformationCircle } from "svelte-hero-icons";
  export let ingress;

  let name = ingress.metadata.name.split("-").filter(a => a != "ingress").pop(0)
  //let name = ingress.metadata.name.replace('ingress', '').replace('--','-').replace(/\-$/, "")
  let rules = ingress.spec.rules
  let hosts = rules.map(r => r.host)
  let paths = rules.map(r => r.http.paths.map(p => p.path || '/')).flat(2)
  let host = ingress.spec.rules[0].host
  let proto = ingress.spec.tls ? "https://" : "http://"
  let labels = Object.keys(ingress.metadata.labels || {})
  let annotes = Object.keys(ingress.metadata.annotations || {})
  let href = proto + host
  let img = ingress.metadata.annotations.imagesrc || ImageUrl(name)
  let showdetails = false;

  let showhide = () => {
    showdetails = !showdetails
  }
</script>
<div class="card shadow-xl">
  <figure>
    <img src={img} alt={name} class="h-32 rounded-xl">
  </figure>
  <div class="card-body items-center text-center">
    <h2 class="card-title">{name}</h2>
    <div class="text-sm">
      <a target="_blank" href={href}>{host}</a>
      <div class="stats-vertical bg-primary text-primary-content rounded-xl">
        <div class="stat">
          <div class="stat-title">Paths</div>
          <span class="stat-value text-xs inline-grid grid-cols-3 gap-4">
            {#each paths as path}
            <a href={href}{path}>{path}</a>
            {/each}
          </span>
          <div class="stat-actions">
            <a href on:click|preventDefault={showhide} title="Show details" class="text-xs float-right text-right">
              <Icon size="32" src="{InformationCircle}" />
            </a>
            <a target="_blank" href={href} class="btn btn-sm btn-success">
              Open {name}
            </a>
          </div>
        </div>
        
        {#if showdetails}
        <div class="container"> 
          <div class="stat">
            <div class="stat-title">Labels</div>
            {#each labels as label}
              <div class="stat-value text-xs text-left">{label}={ingress.metadata.labels[label]}</div>
            {/each}
          </div>
  
          <div class="stat">
            <div class="stat-title">Annotations</div>
            {#each annotes as annote}
              <div class="stat-value text-xs text-left">{annote}: {ingress.metadata.annotations[annote]}</div>
            {/each}
          </div>
        </div>
        {/if}
      </div>
    </div>
  </div>
</div>
