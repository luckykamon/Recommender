import List from './List';
import {useEffect, useState} from "react";
import PropTypes from "prop-types";

const ListElement = (props) => {
    const [list_Element, setList_Element] = useState([]);

    useEffect(() => {
            let requestOptions = {
                method: 'GET',
                redirect: 'follow'
            };

            fetch(process.env.REACT_APP_HOST_API + "/list/" + props.element.toLowerCase(), requestOptions)
                .then(response => response.text())
                .then(result => {
                    setList_Element(JSON.parse(result))
                })
                .catch(error => console.log('error', error));
        }, []
    )

    return (
        <List listValues={list_Element}
              name={props.element.charAt(0).toUpperCase() + props.element.slice(1).toLowerCase()}/>
    )
}

ListElement.propTypes = {
    element: PropTypes.string.isRequired
}

ListElement.defaultProps = {}

export default ListElement