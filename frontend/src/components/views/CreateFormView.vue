<template>
	<div class="create-form-container">
		<div class="container mt-4 d-flex">
			<button class="btn btn-primary ms-auto">Save Form</button>
		</div>

		<div class="container py-5">
			<div class="row g-4">
				<div class="col-md-4">
					<div class="card shadow-sm mb-4">
						<div class="card-header bg-primary text-white">
							<h5 class="mb-0">Field Configuration</h5>
						</div>
						<div class="card-body">
							<div class="mb-3">
								<label for="fieldType" class="form-label">
									Field Type *
								</label>
								<select
									id="fieldType"
									name="type"
									class="form-select"
								>
									<option value="">Select type</option>
									<option value="text">Text</option>
									<option value="email">Email</option>
									<option value="checkbox">Checkbox</option>
									<option value="number">Number</option>
									<option value="textarea">Text Area</option>
									<option value="select">Dropdown</option>
								</select>
							</div>

							<div class="mb-3">
								<label for="fieldLabel" class="form-label">
									Field Label *
								</label>
								<input
									id="fieldLabel"
									name="label"
									type="text"
									class="form-control"
									placeholder="E.g.: Full Name"
								/>
							</div>

							<div class="mb-3">
								<label
									for="fieldDescription"
									class="form-label"
								>
									Description
								</label>
								<input
									id="fieldDescription"
									name="description"
									type="text"
									class="form-control"
									placeholder="Help text for the user"
								/>
							</div>

							<div class="mb-3 form-check">
								<input
									id="required"
									name="required"
									type="checkbox"
									class="form-check-input"
								/>
								<label for="required" class="form-check-label">
									Required field
								</label>
							</div>

							<button class="btn btn-primary w-100">
								Add Field
							</button>
						</div>
					</div>

					<div class="card shadow-sm">
						<div class="card-header bg-dark text-white">
							<h5 class="mb-0">Form Information</h5>
						</div>
						<div class="card-body">
							<div class="mb-3">
								<label for="formDescription" class="form-label">
									Form Description
								</label>
								<textarea
									id="formDescription"
									rows="3"
									class="form-control"
									placeholder="Describe the purpose of this form..."
								></textarea>
							</div>
						</div>
					</div>
				</div>

				<div class="col-md-8">
					<div class="card shadow-sm">
						<div
							class="card-header bg-dark text-white d-flex justify-content-between align-items-center"
						>
							<h5 class="mb-0">Form Preview</h5>
							<span class="badge bg-primary">0 fields</span>
						</div>
						<div class="card-body">
							<div class="text-center py-5">
								<i
									class="bi bi-file-earmark-text fs-1 text-muted d-block mb-3"
								></i>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									width="48"
									height="48"
									fill="currentColor"
									class="bi bi-file-earmark-text text-muted mb-3"
									viewBox="0 0 16 16"
								>
									<path
										d="M5.5 7a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1h-5zM5 9.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5zm0 2a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5z"
									/>
									<path
										d="M9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.5L9.5 0zm0 1v2A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h5.5z"
									/>
								</svg>
								<h6 class="fw-bold text-muted">
									No fields added
								</h6>
								<p class="text-muted">
									Start adding fields to build your form.
								</p>
							</div>

							<div class="mt-4">
								<button class="btn btn-primary btn-lg w-100">
									Submit Form
								</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
