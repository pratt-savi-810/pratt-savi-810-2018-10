**Determine hotspots around NYC for potential public street-level electric car charging station installations.**
- Paul Jarymowycz

Create parameters for charger locations:
 * at street-side city-owned infrastructure location (utility poles, LinkNYC booths, etc.)
 * with existing electrical connection
   * determine some parameters for required load per charger vs available electrical capacity to point
 * distance away from street corner (legal parking spot, not encroaching on crosswalks, etc.)

Required data:
 * utility poles (NYC Open Data has a dataset: Mobile Telecommunication Franchise Poletop Installation Locations)
 * LinkNYC locations (NYC Open Data: LinkNYC Map)
 * find other datasets

Processing:
 * find street corners -> buffer 15ft from corner
 * remove infrastructure locations inside buffer
 * remove infrastructure locations along street segments that have no parking
 * count number of potential charging points along street segments
 * join count to each street segment
 * color-code street segments by number of potential charging sites

**Will hash this out a bit more in the week ahead.**