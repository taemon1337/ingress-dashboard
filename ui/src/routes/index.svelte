<script>
  import IngressCard from '../components/ingress-card.svelte';
  import {fetchIngress} from '../stores/ingresses.js';
</script>
<div class="container mx-auto px-4">
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</div>
<IngressCard/>
{#await fetchIngress}
  <p>Loading...</p>
{:then resp}
  { resp }
{:catch error}
  <p style="color: red">{error}</p>
{/await}
