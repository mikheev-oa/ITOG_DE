CREATE TABLE basic_showcase_one
(   ID_APP                  NUMBER(10, 0)
    , ID_DISPATCHER         NUMBER(10, 0)    
    , ID_DRIVER             NUMBER(10, 0)
    , VIN_NUMB              VARCHAR2(100)
    , STATE_NUMBER          VARCHAR2(30)
    , FUEL_CONSUMPTION      NUMBER(10, 0)
    , TYPE_CAR              VARCHAR2(30)
    , PRICE_KM              NUMBER(10, 0)
    , PERC_DISCOUNT_ON_CARD NUMBER(10, 0)
    , DISCOUNT_CARD         VARCHAR2(20)
    , APP_DT                DATE
    , MONTH_DT              NUMBER(10, 0)
    , YEAR_DT               NUMBER(10, 0)
    , ADR_BOARD             VARCHAR2(50)
    , DISTR_TRAVEL          VARCHAR2(50)
    , FUEL_RATE             NUMBER(20, 0)
    , DISTANCE_ADR_BOARD    NUMBER(20, 0)
    , PRICE_TRIP            NUMBER(20, 0)
    , DRIVER_NAME           VARCHAR2(100) 
    , PERC_DRIVER           NUMBER(10, 0)
    , DISPATCHER_NAME       VARCHAR2(100)
    , PERC_DISPATHER        NUMBER(10, 0)
    , OCTANE_NUMBER         NUMBER(10, 0) 
    , PRICE_CONS            NUMBER(10, 0)
    , EVALUATION_TRIP       NUMBER(15, 0)
 );
 
/
CREATE TABLE basic_showcase_two
(   STATE_NUMBER        VARCHAR2(20)
    , CAR_BRAND         VARCHAR2(50)    
    , VIN_NUMB          VARCHAR2(50)
    , TYPE_CAR          VARCHAR2(20)
    , FUEL_CONSUMPTION  NUMBER(10, 0)
    , OCTANE_NUMBER     NUMBER(10, 0)
    , PRC_SERVICE       NUMBER(30, 0)
    , PRICE_CONS        NUMBER(10, 0)
 );
 
/
CREATE TABLE avg_ratings
(    ID_DRIVER      NUMBER(10, 0)
    , DRIVER_NAME   VARCHAR2(100)
    , MONTH_DT      NUMBER(10, 0)
    , YEAR_DT       NUMBER(10, 0)
    , MONTH_YEAR_DT VARCHAR2(30)
    , AVG_RAT       NUMBER(20, 2)
 );

/
CREATE TABLE basic_car_revenue
(    VIN_NUMB       VARCHAR2(50)
    , STATE_NUMBER  VARCHAR2(20)
    , MONTH_DT      NUMBER(10, 0)
    , YEAR_DT       NUMBER(10, 0)
    , FUEL_RATE     NUMBER(20, 0)
 );
 
/
CREATE TABLE compl_app
(   MONTH_YEAR_DT     VARCHAR2(40)
    , CNT_MONTH_DT    NUMBER(10, 0)
    , CNT_YEAR_DT     NUMBER(10, 0)
 );
 
/
CREATE TABLE disp_earnings
(   ID_DISPATCHER	    NUMBER(20,0)
    , CNT_ORDERS	    NUMBER(20,0)
    , DISPATCHER_NAME	VARCHAR2(100)
    , INCOME_DISP	    NUMBER(20,0)    
 );

/
CREATE TABLE driver_earnings
(   ID_DRIVER	        NUMBER(20,0)
    , CNT_ORDERS	    NUMBER(20,0)
    , DRIVER_NAME	    VARCHAR2(100)
    , INCOME_DRIVER	    NUMBER(20,0)    
 );
 
/
CREATE TABLE number_of_ratings
(   MONTH_DT     NUMBER(10, 0)
    , YEAR_DT    NUMBER(10, 0)
    , EVAL_TRIP  NUMBER(10, 0)
 );
 
/
CREATE TABLE repair_costs_car
(    CAR_BRAND      VARCHAR2(50)
    , CNT_CAR       NUMBER(10, 0)
    , PRC_SERVICE   NUMBER(20, 0)
    , AVG_CHECK     NUMBER(30, 2)
 );
/