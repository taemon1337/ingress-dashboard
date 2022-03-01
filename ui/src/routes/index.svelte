<script>
  import { onMount } from "svelte";
  import { ingressData } from '../stores/ingresses.js';

  onMount(async () => {
    fetch("/data.json")
    .then(response => response.json())
    .then(data => {
      ingressData.set(data.items);
    }).catch(error => {
      console.log(error);
      return [];
    });
  });
  import IngressCard from '../components/ingress-card.svelte';
</script>
<div class="md:container md:mx-auto">
  <div class="grid md:grid-cols-4 sm:grid-cols-3 xs:grid-cols-1 gap-4">
    {#each $ingressData as ingress }
      <IngressCard ingress={ingress} />
    {/each}
  </div>
</div>