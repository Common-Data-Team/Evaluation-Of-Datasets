<script>
    import FusionCharts from 'fusioncharts';
    import Charts from 'fusioncharts/fusioncharts.charts';
    import FusionTheme from 'fusioncharts/themes/fusioncharts.theme.fusion';
    import SvelteFC, {fcRoot} from 'svelte-fusioncharts';

    export let data;
    let chartsSource = [];
    for (let key in data.charts) {
        chartsSource.push({
            chart: {
                caption: key,
                theme: 'fusion'
            },
            data: []
        });
        let values = data.charts[key].data;
        for (let titleKey in values) {
            chartsSource[chartsSource.length-1].data.push({
                label: titleKey,
                value: values[titleKey]
            });
        }
    }

    const chartConfigs = {
        width: '600',
        height: '400',
        dataFormat: 'json',
    }

    fcRoot(FusionCharts, Charts, FusionTheme);

</script>
{#each Object.keys(data.charts) as key, ind}
<div class="chart-block">
    {#if data.charts[key].type == 'bar'}
        <SvelteFC {...chartConfigs} dataSource={chartsSource[ind]} type="column2d"/>
    {:else}
        <SvelteFC {...chartConfigs} dataSource={chartsSource[ind]} type="pie2d"/>
    {/if}
</div>
{/each}

