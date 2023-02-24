import Typography from '@mui/material/Typography';
import ListElement from "./components/List/ListElement";
import Turnover from "./components/Turnover/Turnover";
import BarChart from "./components/Turnover/BarChart";
import {Button} from "@mui/material";
import List from "./components/List/List";
import PropTypes from "prop-types";
import {useEffect, useRef, useState} from "react";
import {useDispatch, useSelector} from "react-redux";
import {getLibelle, setLibelle} from "./components/redux/list";

const App = () => {

    const dispatch = useDispatch();

    const [dataBarChart, setDataBarChart] = useState([]);
    const [nameData, setNameData] = useState("");

    let listNameElement = ["cli_id", "famille", "libelle", "maille", "univers", "prix_net", "mois_vente", "ticket_id"]

    let turnoverNameElement = ["famille", "libelle", "maille", "univers"]

    return (
        <div style={{textAlign: "center"}}>
            <Typography variant="h3" gutterBottom>
                T-DAT-901-REN
            </Typography>
            {/*<Typography variant="p" gutterBottom>*/}
            {/*    List:*/}
            {/*</Typography>*/}
            <br/>
            <div style={{display: "flex", overflowX: "auto"}}>
                {listNameElement.map((elementName) => (
                    <div key={elementName}>
                        <ListElement element={elementName}/>
                        <br/>
                        {turnoverNameElement.includes(elementName) && (
                            <Turnover name={elementName}/>
                        )}
                    </div>
                ))}
            </div>
            <br/>
            <BarChart data={dataBarChart} name={nameData}/>


        </div>
    );
}

List.propTypes = {
    name: PropTypes.string.isRequired,
}

List.defaultProps = {}

export default App;
