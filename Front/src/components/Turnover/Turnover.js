import PropTypes from "prop-types";
import List from "../List/List";
import {Button} from "@mui/material";
import {useDispatch, useSelector} from "react-redux";
import {getNameDataTurnover, setNameDataTurnover} from "../redux/turnover";


const Turnover = (props) => {

    const dispatch = useDispatch();
    const nameData = useSelector(getNameDataTurnover);

    const calculTurnover = () => {


        // let nameData;
        switch (props.name.toLowerCase()) {
            case "libelle":
                dispatch(setNameDataTurnover("libelle"));
                break;
            case "prix_net":
                dispatch(setNameDataTurnover("prix_net"));
                break;
            case "famille":
                dispatch(setNameDataTurnover("famille"));
                break;
            case "univers":
                dispatch(setNameDataTurnover("univers"));
                break;
            case "mois_vente":
                dispatch(setNameDataTurnover("mois_vente"));
                break;
            case "cli_id":
                dispatch(setNameDataTurnover("cli_id"));
                break;
            case "maille":
                dispatch(setNameDataTurnover("maille"));
                break;
            case "ticket_id":
                dispatch(setNameDataTurnover("ticket_id"));
                break;
            default:
                break;

        }
    }

    return (
        <div style={{margin: "10px"}}>
            <Button variant="outlined" fullWidth onClick={calculTurnover}>{"Chiffre d'affaire " + props.name}</Button>
        </div>
    )
}

List.propTypes = {
    name: PropTypes.string.isRequired,
}

List.defaultProps = {}

export default Turnover