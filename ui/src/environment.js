export const environment = () => {
  return {
    IMAGE_API: import.meta.env.VITE_IMAGE_API || "http://images.svc.cluster.local:8080",
    IMAGE_HEIGHT: import.meta.env.VITE_IMAGE_HEIGHT || 32,
    CARD_CLASS: (import.meta.env.VITE_CARD_CLASS || "grid_md:grid-cols-4_sm:grid-cols-3_xs:grid-cols-1_gap-4").replaceAll('_', ' '),
  }
}