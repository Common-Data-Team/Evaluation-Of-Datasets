import Qwe from './routes/qwe.svelte';
import Service from './routes/service.svelte';

export default {
    '/service': Service,
    '/': Qwe,
    '*': Qwe,
}