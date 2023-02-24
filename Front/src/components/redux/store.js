import {configureStore} from '@reduxjs/toolkit';
import counterReducerList from './list';
import counterReducer from './turnover';
import {saveState} from "./localStorage"

const store = configureStore({
    reducer: {
        list: counterReducerList,
        turnover: counterReducer
    },

})

store.subscribe(() => {
    saveState(store.getState())
})


export default store;
