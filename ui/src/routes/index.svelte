<script>
  import IngressCard from '../components/ingress-card.svelte';
</script>
<div class="container mx-auto px-4">
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</div>
<IngressCard/>
<div class="hero min-h-screen bg-base-200">
  <div class="flex-col hero-content lg:flex-row-reverse">
    <img src="https://api.lorem.space/image/movie?w=260&h=400" class="max-w-sm rounded-lg shadow-2xl">
    <div>
      <h1 class="text-5xl font-bold">Box Office News!</h1>
      <p class="py-6">Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem quasi. In deleniti eaque aut repudiandae et a id nisi.</p>
      <button class="btn btn-primary">Get Started</button>
    </div>
  </div>
</div>
