from my_constants import Pokedata


def is_garcs_loaded(poke_edit_data: Pokedata) -> bool:
    return poke_edit_data.model != []
