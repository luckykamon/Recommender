import {useEffect, useState} from "react";
import PropTypes from "prop-types";
import Typography from '@mui/material/Typography';



const Corentin = () => {

    const [data, setData] = useState([]);


    return (
        <div style={{textAlign: "center"}}>
            <Typography variant="h2" gutterBottom>
                Page de test
            </Typography>

            <div>
            test deviation:
             <button onClick={() => {
                    fetch('http://127.0.0.1:3000/deviation/FAMILLE/3/true')
                        .then(response => response.json())
                        // append response to the page
                        .then(data => {
                            setData(data);
                            console.log(data);
                        })
                }}>Get Top 3 Deviation par Famille
                </button>
            <button onClick={() => {
                    fetch('http://127.0.0.1:3000/deviation/MAILLE/10/true')
                        .then(response => response.json())
                        // append response to the page
                        .then(data => {
                            setData(data);
                            console.log(data);
                        })
                }}>Get Top 10 Deviation par Maille
                </button>

            </div>

            <div>
                 <br></br>
                Catégories ET valeurs de deviation :
            {/*    display key and value of data object*/}
                {Object.keys(data).map((key) => {
                    return <div>{key} : {data[key]}</div>

                }
                )}



            </div>

              <div>
                  <br></br>
                  Catégorie Uniquement :
                {/*display just category names from data object*/}
               {Object.keys(data).map((key) => {
                    return <div>{key}</div>

                }
                )}



            </div>

        </div>

    );
}

export default Corentin;

