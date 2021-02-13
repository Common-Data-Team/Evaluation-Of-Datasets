<script>

    let email;

    let hasSubscription = false;

    function submit() {

    }
</script>

<form class="wrapper_inpt">
    <label>
        <input type="email" placeholder="help@commondata.ru" bind:value={email}>
        <button class="btn_area">Подписаться</button>
    </label>
</form>

<style>
    * {
        margin: 0;
        padding: 0;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
        font-family: sans-serif;
        outline: none;
    }

    .wrapper_inpt {
        width: 400px;
        height: 50px;
        border-radius: 20px;
        border: 1px solid #fff;
        background-color: #fff;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0px 8px 80px rgba(0, 0, 0, 0.06);
        padding: 5px;
    }

    .btn_area {
        width: 110px;
        height: 40px;
        background: #1355FF;
        border-radius: 20px;
        color: #fff;
        align-items: center;
        font-size: 12px;
        text-align: center;
        cursor: pointer;
    }

    input {
        border: none;
        background: none;
        width: calc(100% - 84px);
        /*height: 100%;*/
        /*font-size: 16px;*/
        text-indent: 12px;
    }

    label {
        width: 100%;
        display: flex;
        flex-direction: row;
    }

    @media (max-width: 700px) {
        .wrapper_inpt {
            width: 90%;
        }
    }

</style>