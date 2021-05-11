create or replace PROCEDURE MIKHEEV_OA_repair_costs_car
IS
BEGIN
  DELETE FROM repair_costs_car;
  COMMIT;
INSERT INTO repair_costs_car
    (CAR_BRAND, CNT_CAR, PRC_SERVICE, AVG_CHECK)
SELECT  CAR_BRAND
        , CNT_CAR
        , PRC_SERVICE
        , ROUND(S.AVG_CHECK, 2) 
FROM (  SELECT    B.CAR_BRAND
                , D.CNT_CAR
                , SUM(A.PRICE_SERVICE) AS PRC_SERVICE
                , SUM(A.PRICE_SERVICE) / D.CNT_CAR AS AVG_CHECK
        FROM maintenance_prc A 
        LEFT JOIN automobil B ON A.VIN_NUMB = B.VIN_NUMB
        LEFT JOIN ( SELECT  C.CAR_BRAND
                            , COUNT(C.CAR_BRAND) AS CNT_CAR
                    FROM automobil C
                    GROUP BY C.CAR_BRAND) D ON D.CAR_BRAND = B.CAR_BRAND
        GROUP BY B.CAR_BRAND, D.CNT_CAR) S;
    DBMS_OUTPUT.PUT_LINE('Выполнение процедуры завершено. Данные помещены в таблицу repair_costs_car')  ;
    COMMIT;
END MIKHEEV_OA_repair_costs_car;