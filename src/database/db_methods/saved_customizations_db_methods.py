from uuid import uuid4

from DTOs.customization_api_dto import SavedCustomizationDTO
from database.models.saved_customizations_model import SavedCustomizationsModel
from database.shared_db import db
from entities.saved_customization import SavedCustomization


class SavedCustomizationsDbMethods:

    @staticmethod
    def upsert_saved_customization(user_id: str, saved_weapon_id: str, customizations: list[SavedCustomizationDTO]) -> list[SavedCustomization]:
        SavedCustomizationsDbMethods._delete_old_customization(saved_weapon_id)
        models: list[SavedCustomizationsModel] = [SavedCustomizationsModel(id=str(uuid4()),
                                                                           user_id=user_id,
                                                                           saved_weapon_id=saved_weapon_id,
                                                                           customization_id=custom.id,
                                                                           slot_type=custom.slot.value
                                                                           ) for custom in customizations]
        db.session.bulk_save_objects(models)
        db.session.commit()
        return [model.convert_to_entity() for model in models]

    @staticmethod
    def _delete_old_customization(saved_weapon_id: str) -> bool:
        """
        Hard delete
        """
        result: int = db.session.query(SavedCustomizationsModel).filter(SavedCustomizationsModel.saved_weapon_id == saved_weapon_id).delete()
        db.session.commit()
        return result > 0
