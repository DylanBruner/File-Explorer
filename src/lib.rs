use pyo3::prelude::*;
use rust_search::SearchBuilder;

#[pyfunction]
fn f_search(path: &str, query: &str, extension: Option<&str>) -> PyResult<Vec<String>> {
    let ext: String = extension.unwrap_or("*").to_string();
    let search: Vec<String> = SearchBuilder::default()
        .location(path)
        .search_input(query)
        .ignore_case()
        .hidden()
        .ext(ext)
        .build()
        .collect();

    Ok(search)
}

/// A Python module implemented in Rust.
#[pymodule]
fn search(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(f_search, m)?)?;
    Ok(())
}