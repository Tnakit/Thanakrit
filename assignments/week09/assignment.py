def calculate_electricity_cost(units):
    if units < 0:
        print("จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ\n")
        return
 
    u1 = min(units, 50)
    u2 = min(max(0.0, units - 50), 50)
    u3 = min(max(0.0, units - 100), 100)
    u4 = max(0.0, units - 200)
 
    cost1 = u1 * 2.50
    cost2 = u2 * 3.00
    cost3 = u3 * 3.50
    cost4 = u4 * 4.00
    service_fee = 25.00
 
    total_cost = cost1 + cost2 + cost3 + cost4 + service_fee
 
    print("\nรายละเอียดค่าไฟ:")
    if u1 > 0:
        print(f"1-{int(u1)} หน่วย: {cost1:.2f} บาท")
    if u2 > 0:
        print(f"51-{int(50 + u2)} หน่วย: {cost2:.2f} บาท")
    if u3 > 0:
        print(f"101-{int(100 + u3)} หน่วย: {cost3:.2f} บาท")
    if u4 > 0:
        print(f"มากกว่า 200 หน่วย ({int(u4)} หน่วย): {cost4:.2f} บาท")
 
    print(f"ค่าบริการ: {service_fee:.2f} บาท")
    print(f"รวมค่าไฟทั้งสิ้น: {total_cost:.2f} บาท\n")
 
 
