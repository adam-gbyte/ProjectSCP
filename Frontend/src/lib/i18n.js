import { writable, derived } from 'svelte/store';
import { translations } from './translations.js';

// Default language: 'en' (English)
export const locale = writable('en');

// Derived translation function t(key)
export const t = derived(locale, ($locale) => {
  return (key) => {
    const keys = key.split('.');
    let result = translations[$locale];
    for (const k of keys) {
      result = result?.[k];
    }
    return result ?? key;
  };
});

export function toggleLocale() {
  locale.update((l) => (l === 'id' ? 'en' : 'id'));
}
