import {createSlice} from '@reduxjs/toolkit'
import {loadState} from "./localStorage"


export const valueListSlice = createSlice({
    name: 'valueList',
    initialState: loadState()?.list || {
        libelle: "Select Libelle",
        prix_net: "Select Prix_net	",
        famille: "Select Famille",
        univers: "Select Univers",
        mois_vente: "Select Mois_vente",
        cli_id: "Select Cli_id",
        maille: "Select Maille",
        ticket_id: "Select Ticket_id"
    },
    reducers: {
        setLibelle: (state, action) => {
            console.log("setLibelle")
            console.log(state.libelle)
            state.libelle = action.payload;
        },
        setPrix_net: (state, action) => {
            state.prix_net = action.payload;
        },
        setFamille: (state, action) => {
            state.famille = action.payload;
        },
        setUnivers: (state, action) => {
            state.univers = action.payload;
        },
        setMois_vente: (state, action) => {
            state.mois_vente = action.payload;
        },
        setCli_id: (state, action) => {
            state.cli_id = action.payload;
        },
        setMaille: (state, action) => {
            state.maille = action.payload;
        },
        setTicket_id: (state, action) => {
            state.ticket_id = action.payload;
        }
    },
})

export const {setLibelle, setPrix_net, setFamille, setCli_id, setMaille, setMois_vente , setTicket_id, setUnivers, getState} = valueListSlice.actions

// The function below is called a thunk and allows us to perform async logic. It
// can be dispatched like a regular action: `dispatch(incrementAsync(10))`. This
// will call the thunk with the `dispatch` function as the first argument. Async
// code can then be executed and other actions can be dispatched
// export const incrementAsync = (amount) => (dispatch) => {
//     setTimeout(() => {
//         dispatch(incrementByAmount(amount))
//     }, 1000)
// }


export const getLibelle = state => state.list.libelle;
export const getPrix_net = state => state.list.prix_net;
export const getFamille = state => state.list.famille;
export const getUnivers = state => state.list.univers;
export const getMois_vente = state => state.list.mois_vente;
export const getCli_id = state => state.list.cli_id;
export const getMaille = state => state.list.maille;
export const getTicket_id = state => state.list.ticket_id;


export default valueListSlice.reducer
