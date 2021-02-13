<script>
import Qwe from './routes/qwe.svelte';
import Router from 'svelte-spa-router';
import Service from './routes/service.svelte';
const routes = {
    '/': Qwe,
    '/home/*': Service,
    '*': Qwe,
}
</script>
<Router {routes}/>