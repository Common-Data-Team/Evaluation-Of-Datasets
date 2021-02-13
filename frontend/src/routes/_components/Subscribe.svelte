<script>
    import {writable} from 'svelte/store'

    let email;
    let re = /\S+@\S+\.\S+/;
    let span_text = writable('');

    let show_span = false;
    let success = false;
    span_text.subscribe(_ => show_span = true)

    async function submit() {
        if (!re.test(email)){
            $span_text = 'Введите Email';
            success = false;
            return;
        }
        if (localStorage.getItem('hasSubscription')){
            $span_text = 'Вы уже подписаны';
            success = false;
            return;
        }

        let resp = await fetch("https://backendatasets.commondata.ru/email", {
            method: "POST",
            body: JSON.stringify({email: email})
        }).then(r => r.json()).catch(_ => {$span_text = 'Произошла ошибка подключения'; success = false});
        $span_text = 'Вы успешно подписались';
        success = true;
        localStorage.setItem('hasSubscription', 'true')
        return resp;
    }
</script>

<form class="wrapper_inpt">
    <label>
        <input type="email" placeholder="help@commondata.ru" bind:value={email}>
        <button class="btn_area" type="button" on:click={submit}>Подписаться</button>
    </label>
    <p class:show_span class:success>{$span_text}</p>
</form>


<style>
    p {
        opacity: 0;
        margin-top: 15px;
        color: indianred;
        transition: ease 0.7s;
    }
    .success {
        color: #66dd77;
    }
    .show_span {
        opacity: 1;
    }

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
        flex-direction: column;
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