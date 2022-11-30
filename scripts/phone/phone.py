def fix_bolivian_phone(phone: str) -> str:
    phone = phone.replace("+591", '')
    if len(phone) > 8:
        phone = phone.replace("591", '')
    phone = phone.replace(' ', '')
    new_phone = ''.join([i for i in phone if i.isdigit()])
    return new_phone
