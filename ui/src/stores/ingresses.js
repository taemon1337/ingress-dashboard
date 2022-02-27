import { writable, derived } from 'svelte/store';

export const ingressData = writable([]);

export const hostNames = derived(ingressData, ($ingressData) => {
  let hosts = {}
  $ingressData.forEach((ingress) => {
    ingress.spec.rules.forEach((rule) => {
      hosts[rule.host] = 1
    })
  })
  return Object.keys(hosts);
});