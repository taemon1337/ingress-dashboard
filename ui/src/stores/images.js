import { writable, derived } from 'svelte/store';
//import { variables } from '../variables';

export const ImageUrl = (name) => {
  return ["/img", name].join('/')
}