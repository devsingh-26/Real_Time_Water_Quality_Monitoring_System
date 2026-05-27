async function fetchData(){

    const response =
        await fetch("http://127.0.0.1:8000/dashboard")

    const data = await response.json()

    document.getElementById("temperature").innerHTML =
        data.temperature

    document.getElementById("ph").innerHTML =
        data.ph

    document.getElementById("turbidity").innerHTML =
        data.turbidity

    document.getElementById("tds").innerHTML =
        data.tds

    document.getElementById("water_level").innerHTML =
        data.water_level

    document.getElementById("status").innerHTML =
        data.status

    document.getElementById("timestamp").innerHTML =
        data.timestamp

    if(data.status === "UNSAFE"){

        document.getElementById("status").style.color = "red"

    }else{

        document.getElementById("status").style.color = "green"
    }
}

fetchData()

setInterval(fetchData, 2000)