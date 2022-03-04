import { environment } from '../environment';

let env = environment()

export const ImageUrl = (name) => {
  return [env.IMAGE_API, "img", name].join('/').replace('//', '/')
}