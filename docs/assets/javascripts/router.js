/**
 * Smart Link Router
 * 
 * Intercepts clicks on Travelpayouts affiliate links that are currently 
 * returning "marker is not subscribed" errors and automatically redirects 
 * the user to the intended clean, non-affiliate destination.
 * 
 * This allows the site to keep the affiliate structure in the markdown 
 * so that when the site gains traffic and gets approved, this script 
 * can simply be removed.
 */

document.addEventListener('DOMContentLoaded', () => {
    // Listen for all clicks on the document
    document.addEventListener('click', (e) => {
        // Find the closest anchor tag that was clicked
        const link = e.target.closest('a');

        // If not a link, or not an affiliate link, do nothing normal
        if (!link || !link.href.includes('tp.media/r')) return;

        // Specific P_IDs that are currently unapproved
        const unapprovedPartners = [
            'p=121', // Booking.com
            'p=125', // TripAdvisor
            'p=285', // Hotels.com
            'p=170'  // Lonely Planet (though we swapped it out, good to have)
        ];

        const isUnapproved = unapprovedPartners.some(p => link.href.includes(p));

        if (isUnapproved) {
            // Prevent the default Travelpayouts broken redirect
            e.preventDefault();

            // Extract the original destination URL from the 'u=' parameter
            try {
                const urlObj = new URL(link.href);
                const encodedDest = urlObj.searchParams.get('u');
                if (encodedDest) {
                    const cleanUrl = decodeURIComponent(encodedDest);
                    // Redirect directly to the clean URL
                    window.location.href = cleanUrl;
                } else {
                    // Fallback to home if something goes wrong
                    console.warn("Could not find destination in affiliate link");
                    window.location.href = '/';
                }
            } catch (error) {
                console.error("Error parsing affiliate link", error);
            }
        }
    });
});
