import React, {Component} from 'react';
import CanvasJSReact from '../assets/canvasjs.react';

var CanvasJSChart = CanvasJSReact.CanvasJSChart;
var CanvasJS = CanvasJSReact.CanvasJS;
let titleChart = "Chiffre d'affaire par Univers";

var dataForChart = [
    {y: 4000, label: "Janvier"},
    {y: 60000, label: "Février"},
    {y: 42000, label: "Mars"},
    {y: 58000, label: "Avril"},
    {y: 47500, label: "Mai"},
    {y: 48000, label: "Juin"},
    {y: 56000, label: "Juillet"},
    {y: 60000, label: "Août"},
    {y: 50000, label: "Septembre"},
    {y: 60000, label: "Octobre"},
    {y: 42000, label: "Novembre"},
    {y: 58000, label: "Décembre"}

];

let listUnivers = [];

function getListUnivers() {
    return new Promise((resolve, reject) => {
        let requestOptions = {
            method: 'GET',
        };
        fetch("http://localhost:3000/list/univers", requestOptions)
            .then(response => response.text())
            .then(result => {
                listUnivers = JSON.parse(result);
                resolve(listUnivers);
            })
            .catch(error => {
                console.log('error', error)
                reject(error);
            });
    })
}



function getCAByUnivers(universName) {
    return new Promise((resolve, reject) => {
        let test = '';
        if (universName !== null) {
            let requestOptions = {
                method: 'GET',
            };
            fetch("http://localhost:3000/turnover/univers/" + universName, requestOptions)
                .then(response => response.text())
                .then(result => {
                    test = JSON.parse(result);
                    // console.log(test["1"]);
                    putDataInChart(test)
                        .then(res => {
                            resolve(test);
                        })
                        .catch(err => {
                            reject(err);
                        })

                })
                .catch(error => {
                    console.log('error', error)
                    reject(error);
                });
        }
    })


}

function putDataInChart(data) {
    return new Promise((resolve, reject) => {
        let res = [
            {y: data["1"] ? data["1"] : 0, label: "Janvier"},
            {y: data["2"] ? data["2"] : 0, label: "Février"},
            {y: data["3"] ? data["3"] : 0, label: "Mars"},
            {y: data["4"] ? data["4"] : 0, label: "Avril"},
            {y: data["5"] ? data["5"] : 0, label: "Mai"},
            {y: data["6"] ? data["6"] : 0, label: "Juin"},
            {y: data["7"] ? data["7"] : 0, label: "Juillet"},
            {y: data["8"] ? data["8"] : 0, label: "Août"},
            {y: data["9"] ? data["9"] : 0, label: "Septembre"},
            {y: data["10"] ? data["10"] : 0, label: "Octobre"},
            {y: data["11"] ? data["11"] : 0, label: "Novembre"},
            {y: data["12"] ? data["12"] : 0, label: "Décembre"}
        ];
        dataForChart = res;
        resolve(res);
    })

}

class TestGraphInteressant extends Component {

    componentDidMount() {
        getListUnivers()
            .then(res => {
                console.log(res);
                this.forceUpdate();
            })
            .catch(err => {
                console.log(err);
            })
    }

    addSymbols(e) {
        var suffixes = ["", "K", "M", "B"];
        var order = Math.max(Math.floor(Math.log(e.value) / Math.log(1000)), 0);
        if (order > suffixes.length - 1)
            order = suffixes.length - 1;
        var suffix = suffixes[order];
        return CanvasJS.formatNumber(e.value / Math.pow(1000, order)) + suffix;
    }


    render() {

        let options = {


            animationEnabled: true,
            theme: "light2",
            title: {
                text: titleChart
            },


            axisX: {
                title: "Mois",
                reversed: false,

            },
            axisY: {
                title: "Chiffre d'Affaires",
                labelFormatter: this.addSymbols,
                minimum: 0,
            },
            data: [{
                type: "column",
                dataPoints: dataForChart
            }]
        }

        return (

            <div>
                <label htmlFor="Univers">Choisir un univers:</label>
                <select name="Univers" id="Univers" onChange={(e) => {
                    titleChart = "Chiffre d'affaire par mois - " + e.target.value;

                    getCAByUnivers(e.target.value)
                        .then(res => {

                            this.forceUpdate();
                        })
                        .catch(err => {
                            console.log(err);
                        })

                }}>
                    {listUnivers.map((univers, index) => {
                        return <option key={index} value={univers}>{univers}</option>

                    }
                    )}
                </select>


                <CanvasJSChart options={options}
                               onRef={ref => this.chart = ref}
                />

                {/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
            </div>
        );

    }

}

export default TestGraphInteressant;