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
        width: 600,
        height: 400,
        dataFormat: 'json',
    }

    fcRoot(FusionCharts, Charts, FusionTheme);

</script>
<div class="charts-block">
    {#each Object.keys(data.charts) as key, ind}
    <div class="chart">
        {#if data.charts[key].type == 'bar'}
            <SvelteFC {...chartConfigs} dataSource={chartsSource[ind]} type="column2d"/>
        {:else if data.charts[key].type == 'pie'}
            <SvelteFC {...chartConfigs} dataSource={chartsSource[ind]} type="pie2d"/>
        {/if}
    </div>
    {/each}
</div>
<h1>Рекомендации</h1>
<div class="recomendation-block">
    <p>{data.info.miss_by_col}</p>
</div>
<footer></footer>
<style>
    .charts-block {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        margin: 50px auto;
    }

    .chart {
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0px 9.03012px 27.0904px rgba(176, 190, 197, 0.32);
        margin: 25px;
    }

    .recomendation-block {
        width: auto;
        border-radius: 10px;
        box-shadow: 0px 9.03012px 27.0904px rgba(176, 190, 197, 0.32);
        background-color: #FFFFFF;
        margin: 50px auto;
        padding: 50px;
    }

    footer {
        position: absolute;
        bottom: 0;
        height: 50px;
        width: 100%;
        margin-top: 100px;
    }
</style>

