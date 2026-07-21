# Lab 3 Notes

## Function
Function la mot khoi lenh co ten, thuc hien mot cong viec cu the. Function chi chay khi co cho khac goi no - viet dinh nghia function khong lam no
tu chay. 
Vi du: `format_device_label(name, role)` nhan vao ten thiet bi va vai tro, tra ve mot chuoi nhan dang ngan gon nhu `"edge-r1 [router]"`.
Thay vi viet lai logic dinh dang do o nhieu noi trong chuong trinh, minh chi viet mot lan roi goi lai khi can. Function co the co tham so dau vao(parameters), gia tri mac dinh (dung khi nguoi goi khong truyen vao), type hint (bao truoc kieu du lieu dau vao/dau ra), va gia tri `return` tra ve cho noi da goi no.

## Module and Package
Module la mot file Python don le, gom cac dinh nghia lien quan voi nhau. Trong project nay, `formatters.py`, `models.py`, `services.py` moi file
la mot module co mot nhiem vu ro rang (dinh dang chuoi, dinh nghia class Device, dinh nghia class Inventory).

Package la mot thu muc chua nhieu module lien quan, kem theo file `__init__.py` de bao cho Python biet day la mot don vi co the import duoc. Thu muc `netinventory/` chinh la mot package. Viec chia nho thanh module va package giup moi file gon gang, de tim, de test, va cho phep
cac file khac chi import dung phan can dung, khong phai load het toan bo.

## Class vs Object
Class la mot ban thiet ke (blueprint), mo ta thong tin (attribute) va hanh vi (method) ma mot thu se co. `Device` la mot class - no mo ta rang
moi thiet bi se co ten, dia chi IP quan ly, vai tro, nen tang, va trang thai bat/tat, cung voi cac method nhu `label()` va `disable()`.

Object la mot gia tri cu the duoc tao ra tu class do. `edge-r1` va`access-sw1` la 2 object rieng biet cua class `Device` - chung co cung cau truc (theo class dinh nghia) nhung du lieu ben trong khac nhau.

## __init__ and self
`__init__()` la mot method dac biet, tu dong chay moi khi mot object moi duoc tao ra tu class. Nhiem vu cua no la thiet lap gia tri ban dau cho object. Vi du, `Device.__init__()` kiem tra ten va vai tro co hop le khong, chuyen doi dia chi IP, roi luu tat ca thanh cac attribute cua
object.

`self` la tham so co trong moi method, dai dien cho "chinh object dang duoc goi method nay." Khi viet `self.name = name` ben trong `__init__`, minh dang luu gia tri vao dung object nay, khong phai vao class noi chung - do la ly do vi sao `edge-r1` va `access-sw1` co the co ten khac nhau du cung duoc tao tu 1 class.

