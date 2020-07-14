class Solution {
  private int ONE_MINUTE_ANGLE = 6;
  private int ONE_HOUR_ANGLE = 30;
  private int HOURS_ON_CLOCK = 12;
  private double MINUTES_ON_CLOCK = 60.0;

  public double angleClock(int hour, int minutes) {
    double minutesAngle = ONE_MINUTE_ANGLE * minutes;
    double hoursAngle = (hour % HOURS_ON_CLOCK + minutes / MINUTES_ON_CLOCK) * ONE_HOUR_ANGLE;
    double angleBetweenHands = Math.abs(hoursAngle - minutesAngle);
    return Math.min(angleBetweenHands, 360 - angleBetweenHands);
  }
}
