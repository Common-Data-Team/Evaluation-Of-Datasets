import Main from './routes/main.svelte';
import Service from './routes/service.svelte';

export default {
    '/service': Service,
    '/': Main,
    '*': Main,
}