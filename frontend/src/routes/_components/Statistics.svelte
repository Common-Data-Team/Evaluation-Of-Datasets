<script>
    import FusionCharts from 'fusioncharts';
    import Charts from 'fusioncharts/fusioncharts.charts';
    import FusionTheme from 'fusioncharts/themes/fusioncharts.theme.fusion';
    import SvelteFC, {fcRoot} from 'svelte-fusioncharts';

    let missesDict = {
        missed_col_extreme: 'Названия признаков с экстремальной долей пропусков:',
        missed_col_normal: 'Названия признаков с нормальной долей пропусков:',
        missed_col_low: 'Названия признаков с вполне терпимой долей пропусков:'
    }

    export let data;
    console.log(data.info);
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
        {#if data.charts[key].type == 'bar'}
            <div class="chart">
            <SvelteFC {...chartConfigs} dataSource={chartsSource[ind]} type="column2d"/>
            </div>
        {:else if data.charts[key].type == 'pie'}
            <div class="chart">
                <SvelteFC {...chartConfigs} dataSource={chartsSource[ind]} type="pie2d"/>
            </div>
        {/if}
    {/each}
</div>
<h1>Рекомендации</h1>
{#each Object.keys(data.info.missings) as key}
    {#if typeof data.info.missings[key] == 'string' && data.info.missings[key] != ''}
        <div class="recomendation-block">
            <p>{data.info.missings[key]}</p>
        </div>
    {:else if data.info.missings[key].isArray && data.info.missings[key].length != 0}
        <div class="recomendation-block">
            <h1>{missesDict[key]}</h1>
            {#each data.info.missings[key] as signs}
                <div class="misses">
                    <p>{signs}</p>
                </div>
            {/each}
        </div>
    {/if}
{/each}

<footer></footer>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap" rel="stylesheet">
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
        max-width: 700px;
        font-family: 'IBM Plex Sans', sans-serif;
        text-align: left;
        border-radius: 10px;
        box-shadow: 0px 9.03012px 27.0904px rgba(176, 190, 197, 0.32);
        background-color: #FFFFFF;
        margin: 50px auto;
        padding: 30px;
    }

    footer {
        height: 50px;
        width: 100%;
        margin-top: 100px;
    }
</style>

