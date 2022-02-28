import { writable, derived } from 'svelte/store';
import { variables } from '../variables';

export const ImageUrl = (name) => {
  console.log("IMAGE URL IS ", variables.ImageApi, import.meta.env)
  return [variables.ImageApi, "img", name].join('/')
}