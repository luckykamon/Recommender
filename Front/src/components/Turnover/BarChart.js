import React, {Component, useEffect, useRef, useState} from 'react';
import CanvasJSReact from '../../assets/canvasjs.react';
import {useSelector} from "react-redux";
import {getNameDataTurnover, getValueDataTurnover} from "../redux/turnover";

var CanvasJSChart = CanvasJSReact.CanvasJSChart;
var CanvasJS = CanvasJSReact.CanvasJS;

const addSymbols = (e) => {
    var suffixes = ["", "K", "M", "B"];
    var order = Math.max(Math.floor(Math.log(e.value) / Math.log(1000)), 0);
    if (order > suffixes.length - 1)
        order = suffixes.length - 1;
    var suffix = suffixes[order];
    return CanvasJS.formatNumber(e.value / Math.pow(1000, order)) + suffix;
}

// class BarChart extends Component {
//
//     componentDidUpdate(prevProps, prevState) {
//         if (this.props.data !== prevProps.data || this.props.name !== prevProps.name) {
//             this.putDataInChart(this.props.data)
//                 .then(() => {
//                     this.forceUpdate();
//                 })
//         }
//     }
//
//
//     putDataInChart(data) {
//         return new Promise((resolve, reject) => {
//             let res = [
//                 {y: data["1"] ? data["1"] : 0, label: "Janvier"},
//                 {y: data["2"] ? data["2"] : 0, label: "Février"},
//                 {y: data["3"] ? data["3"] : 0, label: "Mars"},
//                 {y: data["4"] ? data["4"] : 0, label: "Avril"},
//                 {y: data["5"] ? data["5"] : 0, label: "Mai"},
//                 {y: data["6"] ? data["6"] : 0, label: "Juin"},
//                 {y: data["7"] ? data["7"] : 0, label: "Juillet"},
//                 {y: data["8"] ? data["8"] : 0, label: "Août"},
//                 {y: data["9"] ? data["9"] : 0, label: "Septembre"},
//                 {y: data["10"] ? data["10"] : 0, label: "Octobre"},
//                 {y: data["11"] ? data["11"] : 0, label: "Novembre"},
//                 {y: data["12"] ? data["12"] : 0, label: "Décembre"}
//             ];
//             dataForChart = res;
//             resolve(res);
//         })
//     }
//
//
//     render() {
//         let options = {
//             animationEnabled: true,
//             theme: "light2",
//             title: {
//                 text: "Chiffre d'affaire par mois en fonction de " + this.props.name
//             },
//             axisX: {
//                 title: "Mois",
//                 reversed: false,
//             },
//             axisY: {
//                 title: "Chiffre d'Affaires selon " + this.props.name,
//                 labelFormatter: addSymbols,
//                 minimum: 0,
//             },
//             data: [{
//                 type: "column",
//                 dataPoints: dataForChart
//             }]
//         }
//
//         if (dataForChart.length === 0) {
//             return (
//                 <div>
//                 </div>
//             )
//         } else {
//             return (
//                 <CanvasJSChart options={options} onRef={ref => this.chart = ref}/>
//             );
//         }
//     }
// }

const BarChart = (props) => {

    const nameDataTurnover = useSelector(getNameDataTurnover);
    const valueDataTurnover = useSelector(getValueDataTurnover);

    var chart = useRef();

    function resultToPointData(result) {
        return [
            {y: result["1"] ? result["1"] : 0, label: "Janvier"},
            {y: result["2"] ? result["2"] : 0, label: "Février"},
            {y: result["3"] ? result["3"] : 0, label: "Mars"},
            {y: result["4"] ? result["4"] : 0, label: "Avril"},
            {y: result["5"] ? result["5"] : 0, label: "Mai"},
            {y: result["6"] ? result["6"] : 0, label: "Juin"},
            {y: result["7"] ? result["7"] : 0, label: "Juillet"},
            {y: result["8"] ? result["8"] : 0, label: "Août"},
            {y: result["9"] ? result["9"] : 0, label: "Septembre"},
            {y: result["10"] ? result["10"] : 0, label: "Octobre"},
            {y: result["11"] ? result["11"] : 0, label: "Novembre"},
            {y: result["12"] ? result["12"] : 0, label: "Décembre"}
        ];
    }

    // The initial values animate, as expected
    const [dataPoints, setDataPoints] = useState([
        {y: props.data["1"] ? props.data["1"] : 0, label: "Janvier"},
        {y: props.data["2"] ? props.data["2"] : 0, label: "Février"},
        {y: props.data["3"] ? props.data["3"] : 0, label: "Mars"},
        {y: props.data["4"] ? props.data["4"] : 0, label: "Avril"},
        {y: props.data["5"] ? props.data["5"] : 0, label: "Mai"},
        {y: props.data["6"] ? props.data["6"] : 0, label: "Juin"},
        {y: props.data["7"] ? props.data["7"] : 0, label: "Juillet"},
        {y: props.data["8"] ? props.data["8"] : 0, label: "Août"},
        {y: props.data["9"] ? props.data["9"] : 0, label: "Septembre"},
        {y: props.data["10"] ? props.data["10"] : 0, label: "Octobre"},
        {y: props.data["11"] ? props.data["11"] : 0, label: "Novembre"},
        {y: props.data["12"] ? props.data["12"] : 0, label: "Décembre"}
    ]);

    const options = {
        animationEnabled: true,
        theme: "light2",
        title: {
            text: "Chiffre d'affaire par mois de :  " + valueDataTurnover + ", en €"
        },
        axisX: {
            title: "Mois",
            reversed: false,
        },
        axisY: {
            title: "Chiffre d'Affaires selon " + valueDataTurnover,
            labelFormatter: addSymbols,
            minimum: 0,
        },
        data: [{
            type: "column",
            dataPoints: dataPoints
        }],
    }

    // This effect simulates dynamic data updates via fetch
    useEffect(() => {
        var myChart = chart.current;
        // setDataPoints([
        //     {label: "apple", y: 25},
        //     {label: "orange", y: 20},
        //     {label: "mango", y: 10},
        //     {label: "grape", y: 5}
        // ]);

        let requestOptions = {
            method: 'GET',
            redirect: 'follow'
        };

        fetch(process.env.REACT_APP_HOST_API + "/turnover/" + nameDataTurnover + "/" + valueDataTurnover, requestOptions)
            .then(response => response.text())
            .then(result => {
                console.log(result);
                setDataPoints(resultToPointData(JSON.parse(result)));
                myChart.render();
            })
            .catch(error => {
                console.log('error', error)
            });


    }, [nameDataTurnover, valueDataTurnover]);

    return (
        <CanvasJSChart
            options={options}
            onRef={ref => (chart.current = ref)}
        />
    );
}

export default BarChart;