import {createSlice} from '@reduxjs/toolkit'
import {loadState} from "./localStorage"


export const valueTurnoverSlice = createSlice({
    name: 'valueTurnover',
    initialState: loadState()?.turnover || {
        nameDataTurnover: "",
    },
    reducers: {
        setNameDataTurnover: (state, action) => {
            state.nameDataTurnover = action.payload;
        },
    },
})

export const {
    setNameDataTurnover
} = valueTurnoverSlice.actions

// The function below is called a thunk and allows us to perform async logic. It
// can be dispatched like a regular action: `dispatch(incrementAsync(10))`. This
// will call the thunk with the `dispatch` function as the first argument. Async
// code can then be executed and other actions can be dispatched
// export const incrementAsync = (amount) => (dispatch) => {
//     setTimeout(() => {
//         dispatch(incrementByAmount(amount))
//     }, 1000)
// }


export const getNameDataTurnover = state => state.turnover.nameDataTurnover;
export const getValueDataTurnover = state => state.list[state.turnover.nameDataTurnover];


export default valueTurnoverSlice.reducer
