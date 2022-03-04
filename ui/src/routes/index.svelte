<script>
  import { onMount } from "svelte";
  import { ingressData } from '../stores/ingresses.js';
  import { environment } from '../environment';

  let env = environment();
  let cardclasses = env.CARD_CLASS;
  // grid md:grid-cols-4 sm:grid-cols-3 xs:grid-cols-1 gap-4

  function sortByIndex(a, b) {
    return (a.metadata.annotations["dashboard-index"] || 100) - (b.metadata.annotations["dashboard-index"] || 100)
  }

  function notHidden(item) {
    return !Object.keys(item.metadata.annotations).includes("dashboard-hide")
  }

  onMount(async () => {
    fetch("/data.json")
    .then(response => response.json())
    .then(data => {
      ingressData.set(data.items.filter(notHidden).sort(sortByIndex))
    }).catch(error => {
      console.log(error);
      return [];
    });
  });
  import IngressCard from '../components/ingress-card.svelte';
</script>
<div class="md:container md:mx-auto">
  <div class={cardclasses}>
    {#each $ingressData as ingress }
      <IngressCard ingress={ingress} />
    {/each}
  </div>
</div>