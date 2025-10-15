# count_vowels.R
# Count vowels in a string with optional Unicode normalization

#' Count vowels in a string
#'
#' @param s character(1) input string
#' @param extended logical(1) If TRUE and stringi is available, normalize and
#'                 strip diacritics so accented vowels are counted as their base.
#' @return integer count of vowels (a/e/i/o/u)
count_vowels <- function(s, extended = TRUE) {
  if (!is.character(s) || length(s) != 1) stop("s must be a single string")

  if (isTRUE(extended) && requireNamespace("stringi", quietly = TRUE)) {
    s2 <- stringi::stri_trans_nfkd(s)
    s2 <- gsub("\\p{M}", "", s2, perl = TRUE)
  } else {
    if (isTRUE(extended)) {
      warning("stringi not available; falling back to ASCII-only matching")
    }
    s2 <- s
  }

  matches <- gregexpr("[aeiouAEIOU]", s2, perl = TRUE)[[1]]
  if (length(matches) == 1 && matches[1] == -1) return(0L)
  length(matches)
}

# Examples
# print(count_vowels("Hello, World!"))  # -> 3
# print(count_vowels("Résumé", extended = TRUE))  # -> 3 (if stringi available)
