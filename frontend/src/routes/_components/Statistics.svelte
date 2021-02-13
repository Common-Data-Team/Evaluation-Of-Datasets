<script>
    export let data;
</script>

{#each Object.keys(data.charts) as chart}
    <p>{chart}</p>
{/each}