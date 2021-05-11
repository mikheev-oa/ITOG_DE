create or replace PROCEDURE MIKHEEV_OA_BASIC_SHOWCASE_ONE
IS
BEGIN
    Delete from basic_showcase_one;
    commit;
INSERT INTO basic_showcase_one
(   ID_APP, ID_DISPATCHER, ID_DRIVER, VIN_NUMB, STATE_NUMBER, FUEL_CONSUMPTION, TYPE_CAR, PRICE_KM, PERC_DISCOUNT_ON_CARD
    , DISCOUNT_CARD, APP_DT, MONTH_DT, YEAR_DT, ADR_BOARD, DISTR_TRAVEL, FUEL_RATE, DISTANCE_ADR_BOARD, PRICE_TRIP, DRIVER_NAME
    , PERC_DRIVER, DISPATCHER_NAME, PERC_DISPATHER, OCTANE_NUMBER, PRICE_CONS, EVALUATION_TRIP )
SELECT  A.ID_APP
        , A.ID_DISPATCHER
        , A.ID_DRIVER
        , B.VIN_NUMB
        , J.STATE_NUMBER AS STATE_NUMBER
        , J.FUEL_CONSUMPTION
        , J.TYPE_CAR
        , H.PRICE_KM
        , H.PERC_DISCOUNT_ON_CARD AS PRC_DISCOUNT
        , A.DISCOUNT_CARD
        , A.APP_DT
        , EXTRACT (MONTH FROM A.APP_DT) AS MONTH_DT
        , EXTRACT (YEAR FROM A.APP_DT) AS YEAR_DT
        , A.ADR_BOARD
        , A.DISTR_TRAVEL
        , CASE
            WHEN F.PRICE_TRIP > 0 AND A.DISCOUNT_CARD = '���' THEN F.PRICE_TRIP
            WHEN F.PRICE_TRIP > 0 AND A.DISCOUNT_CARD = '��' THEN F.PRICE_TRIP - (F.PRICE_TRIP * (H.PERC_DISCOUNT_ON_CARD / 100))
            WHEN E.DISTANCE_ADR_BOARD > 0 AND A.DISCOUNT_CARD = '���' THEN E.DISTANCE_ADR_BOARD * H.PRICE_KM
            WHEN E.DISTANCE_ADR_BOARD > 0 AND A.DISCOUNT_CARD = '��' THEN (E.DISTANCE_ADR_BOARD * H.PRICE_KM) - ((E.DISTANCE_ADR_BOARD * H.PRICE_KM) * (H.PERC_DISCOUNT_ON_CARD / 100)) 
          END AS FUEL_RATE
        , E.DISTANCE_ADR_BOARD AS DIST_REGTON_TRIP
        , F.PRICE_TRIP AS PRICE_TRIP_AREA
        , B.SURNAME_DR || ' ' || B.NAME_DR || ' ' || B.PATRONYMIC_DR AS DRIVER_NAME
        , B.PERC_PAYMENT_WORK AS PERC_DRIVER
        , C.SURNAME_DS || ' ' || C.NAME_DS || ' ' || C.PATRONYMIC_DS AS DISPATCHER_NAME
        , C.PERC_PAYMENT_WORK AS PERC_DISPATHER
        , J.OCTANE_NUMBER
        , K.PRICE_CONS
        , A.EVALUATION_TRIP  
FROM app_licat A 
LEFT JOIN drivers_lst B ON B.ID_DRIVER = A.ID_DRIVER 
LEFT JOIN dispatcher C ON A.ID_DISPATCHER = C.ID_DISPATCHER
LEFT JOIN price_distinct D ON A.DISTR_TRAVEL = D.CITY_DISTRICT 
LEFT JOIN area_distance E ON A.DISTR_TRAVEL = E.AREA_ITEM
LEFT JOIN price_distinct F ON A.DISTR_TRAVEL = F.CITY_DISTRICT
LEFT JOIN automobil J ON B.VIN_NUMB = J.VIN_NUMB
LEFT JOIN price_kilometer H ON J.TYPE_CAR = H.TYPE_CAR
LEFT JOIN consumption_price K ON J.OCTANE_NUMBER = K.OCTANE_NUMBER ;    
    DBMS_OUTPUT.PUT_LINE('���������� ��������� ���������! ������ �������� � ������� basic_showcase_one')  ;
    COMMIT;
END MIKHEEV_OA_basic_showcase_one;