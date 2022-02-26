import { writable } from 'svelte/store';

export const ingresses = writable([]);

export const fetchIngress = async () => {
  return fetch('/data.json');
};
