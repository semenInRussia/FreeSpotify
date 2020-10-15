import axios from "axios";

const base_artist_detail_url = "http://127.0.0.1:8000/api/artists/"

export default {
    state: {
        artist_info: {}
    },
    getters: {
        artist(state) {
            return state.artist_info
        }
    },
    actions: {
        fetchArtistInfo(ctx, artist_name) {
            const artist_detail_url = base_artist_detail_url + artist_name
            let artist_info;

            axios.get(artist_detail_url)
                .then((res) => {
                    artist_info = res
                });
            ctx.commit("setArtistInfo", artist_info)
        }
    },
    mutations: {
        setArtistInfo(state, artist_info) {
            state.artist_info = artist_info
        }
    }
}