-- Import as job_listings
SELECT role, COUNT(*) listing_count FROM job_listings
GROUP BY role ORDER BY listing_count DESC;

SELECT role, ROUND(AVG(annual_ctc_lpa),2) average_sample_ctc_lpa
FROM job_listings GROUP BY role ORDER BY average_sample_ctc_lpa DESC;

SELECT experience_level, COUNT(*) listing_count
FROM job_listings GROUP BY experience_level ORDER BY listing_count DESC;
