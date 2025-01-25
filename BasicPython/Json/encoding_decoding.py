import json

def custom_json(obj):
    if isinstance(obj, complex):
        return {"__complex__": True, "real": obj.real, "imag": obj.imag}
    raise TypeError(f'Cannot serialize object of {type(obj)}')

print(json.dumps(1 + 2j, default=custom_json))

def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct

print(json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex))