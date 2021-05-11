create or replace PROCEDURE MIKHEEV_OA_basic_car_revenue
IS
BEGIN
  DELETE FROM basic_car_revenue;
  COMMIT;
INSERT INTO basic_car_revenue
    (VIN_NUMB, STATE_NUMBER, MONTH_DT, YEAR_DT, FUEL_RATE )
SELECT 
    VIN_NUMB
    , STATE_NUMBER
    , MONTH_DT
    , YEAR_DT
    , SUM(FUEL_RATE) AS FUEL_RATE
FROM basic_showcase_one
GROUP BY STATE_NUMBER, MONTH_DT, YEAR_DT, VIN_NUMB
ORDER BY YEAR_DT ASC;
    DBMS_OUTPUT.PUT_LINE('Выполнение процедуры завершено. Данные помещены в таблицу BASIC_CAR_REVENUE')  ;
    COMMIT;
END MIKHEEV_OA_basic_car_revenue;