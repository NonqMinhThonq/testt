        Hướng dẫn và mô tả dự án.

tài khoản mật khẩu test
  "username": "admin",
  "password": "admin"

--> Các chức năng có trong dự án:
- thao tác CRUD 
- phân trang và tìm kiếm dữ liệu trong trang
- quản lý admin page, thêm các chức năng tìm kiếm và lọc dữ liệu trong admin page.

--> trang admin
- admin page: https://testt-xl4y.onrender.com/admin/

--> xác thực người dùng và lấy Token( Token có thời hạn là 1 ngày):
- https://testt-xl4y.onrender.com/api/token/
{
  "username": "admin",
  "password": "admin"
}

--> Tương tác với bảng Taskboard (POST, PUT, PATCH, GET, DELETE):
- POST: https://testt-xl4y.onrender.com/api/taskboards/
- cập nhật dữ liệu PUT: https://testt-xl4y.onrender.com/api/taskboards/{id}/
- cập nhật phần dữ liệu cần thiết PATCH: https://testt-xl4y.onrender.com/api/taskboards/{id}/ 
- lấy tất dữ liệu GET (phân trang theo số lượng page_size truyền vào, tìm kiếm trong trang theo search = title hay description): https://testt-xl4y.onrender.com/api/taskboards/
- lấy theo id cần thiết GET: https://testt-xl4y.onrender.com/api/taskboards/{id}/ 
- xóa dữ liệu DELETE: https://testt-xl4y.onrender.com/api/taskboards/{id}/

--> Tương tác với bảng Customer (POST, PUT, PATCH, GET, DELETE):
- POST: https://testt-xl4y.onrender.com/api/customers/
- cập nhật dữ liệu PUT: https://testt-xl4y.onrender.com/api/customers/{id}/
- cập nhật phần dữ liệu cần thiết PATCH: https://testt-xl4y.onrender.com/api/customers/{id}/ 
- lấy tất dữ liệu GET: https://testt-xl4y.onrender.com/api/customers/
- lấy theo id cần thiết GET: https://testt-xl4y.onrender.com/api/customers/{id}/
- xóa dữ liệu DELETE: https://testt-xl4y.onrender.com/api/customers/{id}/

--> Tương tác với bảng Product (POST, PUT, PATCH, GET, DELETE):
- POST: https://testt-xl4y.onrender.com/api/products/
- cập nhật dữ liệu PUT: https://testt-xl4y.onrender.com/api/products/{id}/
- cập nhật phần dữ liệu cần thiết PATCH: https://testt-xl4y.onrender.com/api/products/{id}/ 
- lấy tất dữ liệu GET: https://testt-xl4y.onrender.com/api/products/
- lấy theo id cần thiết GET: https://testt-xl4y.onrender.com/api/products/{id}/ 
- xóa dữ liệu DELETE: https://testt-xl4y.onrender.com/api/products/{id}/

--> Tương tác với bảng Employee (POST, PUT, PATCH, GET, DELETE):
- POST: https://testt-xl4y.onrender.com/api/employees/
- cập nhật dữ liệu PUT: https://testt-xl4y.onrender.com/api/employees/{id}/
- cập nhật phần dữ liệu cần thiết PATCH: https://testt-xl4y.onrender.com/api/employees/{id}/ 
- lấy tất dữ liệu GET: https://testt-xl4y.onrender.com/api/employees/
- lấy theo id cần thiết GET: https://testt-xl4y.onrender.com/api/employees/{id}/ 
- xóa dữ liệu DELETE: https://testt-xl4y.onrender.com/api/employees/{id}/
