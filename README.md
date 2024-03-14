
class BonusCallResult {
    public boolean success;
    public String stock_number;
    public Float dividend;
    public Float dividend_yield;
    public String exDividendDate;
    public String dividendPaymentDate;
    public String meetingDate;
}

class BonusCallPayload {
    public String version;
    public BonusCallResult result;

}