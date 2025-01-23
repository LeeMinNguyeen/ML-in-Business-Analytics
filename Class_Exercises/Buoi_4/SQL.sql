/*
Câu 1: Chọn tất cả sản phẩm
*/
select *
from product

/*
Câu 2: Xếp sản phẩm theo đơn giá giảm dần
*/
SELECT *
FROM PRODUCT
ORDER by price desc

/*
Câu 3: Xuất sản phẩm có cột thành tiền sắp xếp tăng dần
*/
SELECT *, (price * amount) as totalprice
FROM PRODUCT
ORDER BY totalprice asc

/*
Câu 4: Viết SQL lấy toàn bộ danh mục
*/
SELECT * FROM category

/*
Câu 5: Lọc ra các sp thuộc 1 danh mục bất kỳ
*/
SELECT * FROM product
where categoryid = 1

/*
Câu 6: Lọc ra các hóa đơn của 1 khách hàng bất kỳ
*/
SELECT * FROM bill
where customerid = 1

/*
Câu 7: Xuất khách hàng có số hóa đơn nhiều nhất
*/
SELECT customerid, count(*) as billcount FROM bill
GROUP BY customerid
order by billcount desc

/*
Câu 8: Xuất khách hàng có số hóa đơn cao nhất
*/
select b.customerid, sum(bd.amount * bd.price) as totalprice
from bill b
join billdetail bd on b.id = bd.billid
group by b.customerid
order by totalprice desc
limit 1;

/*
Câu 9: Chức năng đăng nhập cho nhân viên
*/
SELECT employee
where username = 'nameemployee' and password = '123'

select * from employee where username='nguyin' and password='nguyin'