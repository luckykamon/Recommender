import PropTypes from "prop-types"
import {FormControl, Select, TextField} from "@mui/material";
import {useState} from "react";
import {useSelector, useDispatch} from 'react-redux';
import {
    getLibelle,
    getMaille,
    getMois_vente,
    getPrix_net,
    getTicket_id,
    getUnivers,
    getFamille,
    getCli_id,
    setLibelle,
    setCli_id,
    setMaille,
    setFamille,
    setMois_vente,
    setPrix_net,
    setTicket_id,
    setUnivers
} from '../redux/list';

const List = (props) => {

    const dispatch = useDispatch();

    const libelle = useSelector(getLibelle);
    const prix_net = useSelector(getPrix_net);
    const famille = useSelector(getFamille);
    const univers = useSelector(getUnivers);
    const mois_vente = useSelector(getMois_vente);
    const cli_id = useSelector(getCli_id);
    const maille = useSelector(getMaille);
    const ticket_id = useSelector(getTicket_id);

    const SelectElement = "Select " + props.name

    function defaultValue() {
        let props_name_localStorage;
        switch (props.name.toLowerCase()) {
            case "libelle":
                props_name_localStorage = libelle;
                break;
            case "prix_net":
                props_name_localStorage = prix_net;
                break;
            case "famille":
                props_name_localStorage = famille;
                break;
            case "univers":
                props_name_localStorage = univers;
                break;
            case "mois_vente":
                props_name_localStorage = mois_vente;
                break;
            case "cli_id":
                props_name_localStorage = cli_id;
                break;
            case "maille":
                props_name_localStorage = maille;
                break;
            case "ticket_id":
                props_name_localStorage = ticket_id;
                break;
            default:
                props_name_localStorage = SelectElement;
        }
        // let props_name_localStorage = localStorage.getItem(props.name.toLowerCase())
        if (!isNaN(props_name_localStorage)) {
            props_name_localStorage = parseInt(props_name_localStorage)
        }
        let index = props.listValues.indexOf(props_name_localStorage)
        if (index !== -1) {
            return props.listValues[index];
        } else if (props.listValues.length > 0) {
            return SelectElement;
        } else {
            return "Loading...";
        }
    }

    const [value, setValue] = useState(defaultValue());

    function defaultListValues() {
        if (props.listValues.length > 0) {
            return props.listValues;
        } else {
            return ["Loading..."];
        }
    }

    const [listValue, setListValue] = useState(defaultListValues());

    const onInputSearch = (event) => {
        setListValue(props.listValues.filter((item) => item.toString().includes(event.target.value)).sort());
    }

    const onChangeSelect = (event) => {
        //Update the value
        switch (props.name.toLowerCase()) {
            case "libelle":
                dispatch(setLibelle(event.target.value));
                break;
            case "prix_net":
                dispatch(setPrix_net(event.target.value));
                break;
            case "famille":
                dispatch(setFamille(event.target.value));
                break;
            case "univers":
                dispatch(setUnivers(event.target.value));
                break;
            case "mois_vente":
                dispatch(setMois_vente(event.target.value));
                break;
            case "cli_id":
                dispatch(setCli_id(event.target.value));
                break;
            case "maille":
                dispatch(setMaille(event.target.value));
                break;
            case "ticket_id":
                dispatch(setTicket_id(event.target.value));
                break;
            default:
                console.log("Error: " + props.name.toLowerCase())
        }
        setValue(event.target.value);
    }

    // C'est un peu le onChange de props.listValues
    if (props.listValues.length > 0 && (listValue.length === 0 || listValue[0] === "Loading...")) {
        setListValue(defaultListValues());
        setValue(defaultValue());
    }

    let listValueSlice = listValue.slice(0, 15)

    return (
        <FormControl style={{minWidth: "200px"}} fullWidth>
            <TextField style={{margin: "10px"}} placeholder={"Search " + props.name}
                       onChange={onInputSearch}></TextField>
            <Select
                autoWidth
                native
                value={value}
                onChange={onChangeSelect}
                style={{margin: "10px"}}
            >
                <option key={-1} value={SelectElement}>
                    {SelectElement}
                </option>
                {listValueSlice.includes(value) !== -1 && value !== SelectElement && (
                    <option key={value} value={value}>
                        {value}
                    </option>
                )}
                {listValueSlice.map((name) => (
                    <option key={name} value={name}>
                        {name}
                    </option>
                ))}
            </Select>

        </FormControl>
    )

}

List.propTypes = {
    listValues: PropTypes.array,
    name: PropTypes.string,
}

List.defaultProps = {
    listValues: ["No values"],
    name: "List",
}

export default List