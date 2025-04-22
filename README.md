# HR-Management-System

# Odoo Docker Workspace

## Mô tả

Đây là một workspace được cấu hình để phát triển và triển khai các module Odoo. Workspace này bao gồm các thành phần chính như sau:

- **docker-compose.yml**: Tệp cấu hình Docker Compose để khởi chạy các dịch vụ cần thiết như Odoo và PostgreSQL.
- **pg_password.txt**: Tệp chứa mật khẩu cho cơ sở dữ liệu PostgreSQL.
- **addons/**: Thư mục chứa các module Odoo tùy chỉnh.
- **config/**: Thư mục chứa tệp cấu hình Odoo.
- **oca_reporting_engine/**: Bộ module từ OCA (Odoo Community Association) liên quan đến báo cáo.
- **odoo-data/** và **postgresql-data/**: Thư mục lưu trữ dữ liệu của Odoo và PostgreSQL.

## Cấu trúc thư mục

```
/home/huynhchau/odoo-docker
├── docker-compose.yml
├── pg_password.txt
├── addons/
│   ├── hr_management_mini/
│   │   ├── __init__.py
│   │   ├── __manifest__.py
│   │   ├── ...
├── config/
│   ├── odoo.conf
├── oca_reporting_engine/
│   ├── __init__.py
│   ├── __manifest__.py
│   ├── README.md
│   ├── ...
├── odoo-data/
├── postgresql-data/
├── reporting-engine/
│   ├── LICENSE
│   ├── README.md
│   ├── requirements.txt
│   ├── ...
```

## Hướng dẫn sử dụng

1. **Cài đặt Docker và Docker Compose**:
   - Đảm bảo rằng Docker và Docker Compose đã được cài đặt trên hệ thống của bạn.

2. **Khởi chạy các dịch vụ**:
   - Chạy lệnh `sudo dockercompose up -d` để khởi động các container.

3. **Truy cập Odoo**:
   - Mở trình duyệt và truy cập `http://localhost:8069` để sử dụng Odoo.

4. **Phát triển module**:
   - Thêm các module tùy chỉnh vào thư mục `addons/`.
   - Khởi động lại container Odoo để áp dụng thay đổi.

## Ghi chú

- Đảm bảo rằng bạn đã cấu hình đúng tệp `odoo.conf` trong thư mục `config/`.
- Sử dụng `pg_password.txt` để lưu trữ mật khẩu cơ sở dữ liệu một cách an toàn.

## Liên hệ

gmail:chau25202@gmail.com
