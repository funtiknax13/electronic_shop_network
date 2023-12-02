from rest_framework.exceptions import ValidationError


class CompanyLevelValidation:

    def __call__(self, value):
        tmp_network_type = dict(value).get('network_type')
        tmp_provider = dict(value).get('provider')
        tmp_level = dict(value).get('level')

        if tmp_network_type == 'FC' and tmp_level != 0:
            raise ValidationError('Звено "Завод" всегда 0-го уровня!')

        if tmp_provider:
            if tmp_level - tmp_provider.level != 1:
                raise ValidationError('Поставщик должен быть предыдущим по иерархии объектом сети')
